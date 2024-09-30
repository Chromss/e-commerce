import java.io.*;
import java.util.*;

public class TP1 {
    private static InputReader in;
    private static PrintWriter out;

    static int N, M, Q;
    static long[] P, H, V, qry1, qry2;
    static char[] qry;
    static long[][][] dp;
    static ArrayList<Integer>[][][] indc;
    static String[] fnl;
    
    static int x = 0;
    static PriorityQueue<Customer> line = new PriorityQueue<>(
        Comparator.<Customer>comparingLong(p -> -p.balance).thenComparingLong(p -> p.patience).thenComparingLong(p -> p.id));
    static Stack<Long> disc = new Stack<>();

    static long maxCap = -1;
    static byte typeO = 0;
    static ArrayList<Long> allO = new ArrayList<>();
    static ArrayList<Integer> idxO = new ArrayList<>();

    public static void main(String[] args) {
        InputStream inputStream = System.in;
        in = new InputReader(inputStream);
        OutputStream outputStream = System.out;
        out = new PrintWriter(outputStream);

        // Initiate
        N = in.nextInteger();
        M = in.nextInteger();
        Q = in.nextInteger();

        P = new long[N];
        H = new long[M];
        V = new long[M];
        qry = new char[Q];
        qry1 = new long[Q];
        qry2 = new long[Q];
        fnl = new String[Q];

        for (int i = 0; i < N; i++) P[i] = in.nextLong();
        for (int i = 0; i < M; i++) H[i] = in.nextLong();
        for (int i = 0; i < M; i++) V[i] = in.nextLong();
        handleQuery();

        // Main Program
        while (x < Q) {
            cycle();
            if (qry[x] == 'A') fnl[x] = String.valueOf(handleA());
            else if (qry[x] == 'B') fnl[x] = String.valueOf(handleB());
            else if (qry[x] == 'D') fnl[x] = String.valueOf(handleD());
            else if (qry[x] == 'L') fnl[x] = String.valueOf(handleL());
            else if (qry[x] == 'S') fnl[x] = String.valueOf(handleS());
            else if (qry[x] == 'O') typeO = (qry1[x] == 1) ? (byte) 1 : 2;
            x++;
        }
        if (typeO != 0) handleO();
        for (String str : fnl) out.println(str);
        out.close();
    }

    // Handle All Queue
    public static long handleA() {
        Customer cust = new Customer(qry1[x], qry2[x]);
        line.offer(cust);
        return cust.id;
    }

    public static long handleB() {
        Customer cust = line.peek();
        if (cust == null) return -1;

        long cash = cust.balance;
        long cost = findHighest(P, cash);
        if (cost == -1) {
            line.poll();
            return cust.id;
        } else {
            if (cash == cost) {
                if (!disc.isEmpty()) cost = Math.max(1, cost - disc.pop());
            } else disc.push(cash - cost);
            cust.pay(cost);
            cust.reset();
            line.remove(cust);
            line.offer(cust);
            return cash - cost;
        }
    }
    
    public static long handleD() {
        disc.push(qry1[x]);
        return disc.size();
    }

    public static long handleL() {
        boolean chk = false;
        Customer temp = null;
        Iterator<Customer> it = line.iterator();
        while (it.hasNext()) {
            Customer cust = it.next();
            if (cust.id == qry1[x]) {
                chk = true;
                temp = cust;
                it.remove();
                break;
            }
        }
        return chk ? temp.balance : -1;
    }

    public static long handleS() {
        return findDiff(P, qry1[x]);
    }

    public static void handleO() {
        int k = 0;
        ArrayList<String> resO = (typeO == 1) ? processO1(maxCap) : processO2(maxCap);
        for (int i : idxO) fnl[i] = resO.get(k++);
    }

    // Helper Method
    public static void handleQuery() {
        for (int i = 0; i < Q; i++) {
            String s = in.next();
            if (s.equals("A") || s.equals("O")) {
                qry[i] = s.charAt(0);
                qry1[i] = in.nextLong();
                qry2[i] = in.nextLong();
                if (s.equals("O")) {
                    idxO.add(i);
                    allO.add(qry2[i]);
                }
                if (s.equals("O") && qry2[i] > maxCap) maxCap = qry2[i];
            } else if (s.equals("D") || s.equals("L") || s.equals("S")) {
                qry[i] = s.charAt(0);
                qry1[i] = in.nextLong();
            } else if (s.equals("B")) {
                qry[i] = s.charAt(0);
            }
        }
    }

    public static void cycle() {
        Iterator<Customer> it = line.iterator();
        while (it.hasNext()) {
            Customer cust = it.next();
            cust.nextTurn();
            if (cust.patience == 0) {
                it.remove();
            }
        }
    }

    public static long findHighest(long[] arr, long num) {
        long left = 0;
        long right = arr.length - 1;
        long best = -1;
        
        while (left <= right) {
            long mid = left + (right - left) / 2;
            if (arr[(int) mid] == num) {
                best = arr[(int) mid];
                return (long) best;
            } else if (arr[(int) mid] < num) {
                best = arr[(int) mid];
                left = mid + 1;
            } else right = mid - 1;
        }
        return (long) best;
    }

    public static long findDiff(long[] arr, long num) {
        long left = 0;
        long right = arr.length - 1;
        long closest = arr[0];
        
        while (left <= right) {
            int mid = (int) (left + (right - left) / 2);
            if (Math.abs(arr[mid] - num) < Math.abs(closest - num)) closest = arr[mid];
            if (arr[mid] == num) return 0;
            else if (arr[mid] < num) left = mid + 1;
            else right = mid - 1;
        }
        return Math.abs((long) (closest - num));
    }

    public static ArrayList<String> processO1(long caps) {
        ArrayList<String> res = new ArrayList<>();
        dp = new long[(int) (V.length + 1)][(int) (caps + 1)][3];
    
        for (int x = 0; x <= V.length; x++) {
            for (int y = 0; y <= caps; y++) {
                for (int z = 0; z < 3; z++) {
                    if (x == 0 || y == 0) {
                        dp[x][y][z] = 0;
                    } else {
                        dp[x][y][z] = dp[x - 1][y][0];
                        if (H[x - 1] <= y && z < 2) {
                            dp[x][y][z] = Math.max(dp[x][y][z], V[x - 1] + dp[x - 1][y - (int) H[x - 1]][z + 1]);
                        }
                    }
                }
            }
        }
    
        for (long num : allO) {
            res.add(String.valueOf(dp[(int) V.length][(int) num][0]));
        }
        return res;
    }
    
    @SuppressWarnings("unchecked")
    public static ArrayList<String> processO2(long caps) {
        ArrayList<String> res = new ArrayList<>();
        dp = new long[(int) (V.length + 1)][(int) (caps + 1)][3];
        indc = new ArrayList[(int) (V.length + 1)][(int) (caps + 1)][3];
        
        for (int x = 0; x <= V.length; x++) {
            for (int y = 0; y <= caps; y++) {
                for (int z = 0; z < 3; z++) {
                    indc[x][y][z] = new ArrayList<>();
                }
            }
        }
        
        for (int x = 0; x <= V.length; x++) {
            for (int y = 0; y <= caps; y++) {
                for (int z = 0; z < 3; z++) {
                    if (x == 0 || y == 0) {
                        dp[x][y][z] = 0;
                        indc[x][y][z].clear();
                    } else {
                        dp[x][y][z] = dp[x - 1][y][0];
                        indc[x][y][z] = new ArrayList<>(indc[x - 1][y][0]);
        
                        if (H[x - 1] <= y && z < 2) {
                            long newVal = V[x - 1] + dp[x - 1][y - (int) H[x - 1]][z + 1];
                            if (newVal > dp[x][y][z]) {
                                dp[x][y][z] = newVal;
                                indc[x][y][z] = new ArrayList<>(indc[x - 1][y - (int) H[x - 1]][z + 1]);
                                indc[x][y][z].add(x);
                            }
                        }
                    }
                }
            }
        }
    
        for (long num : allO) {
            long maxVal = dp[(int) V.length][(int) num][0];
            ArrayList<Integer> resIndc = indc[(int) V.length][(int) num][0];
            ArrayList<String> tempIdx = new ArrayList<>();
            
            for (int idx : resIndc) tempIdx.add(String.valueOf(idx));
            res.add(maxVal + " " + String.join(" ", tempIdx));
        }
        return res;
    }    

    // Helper Class
    static class Customer {
        private static long cnt = 0;
        long id;
        long balance;
        long patience;
        long initial;

        public Customer(long balance, long patience) {
            this.id = cnt++;
            this.balance = balance;
            this.patience = patience;
            this.initial = patience;
        }

        public void nextTurn() {
            patience--;
        }

        public void reset() {
            patience = initial;
        }

        public void pay(long num) {
            balance -= num;
        } 
    }

    // Faster Input and Output
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInteger() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }
    }
}
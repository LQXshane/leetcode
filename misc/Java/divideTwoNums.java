// 29. Divide Two Numbers
class divideTwoNums {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE) {
            if (divisor == -1) return Integer.MAX_VALUE;
        }

        long x = dividend < 0 ? -(long) dividend : (long) dividend;
        long y = divisor < 0 ? -(long) divisor: (long) divisor;

        int quotient = helper(x, y, 1);
        if (dividend < 0 && divisor < 0 ) return quotient;
        if (dividend < 0 || divisor < 0 ) return -quotient;
        return quotient;
    }

    public int helper(long x, long y, int count) {
        if (x <= 0 || count == 0) return 0;
        if (y > x) return helper(x, y >>> 1, count >>> 1);
        else return helper(x - y, y + y, count + count) + count;
    }
}

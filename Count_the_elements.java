class Solution
{
    public static int[] countElements(int a[], int b[], int n, int query[], int q)
    {
        int[] result = new int[q];
        for (int i = 0; i < q; i++) {
            int c = 0;
            for (int j = 0; j < b.length; j++) {
                if (b[j] <= a[query[i]]) {
                    c++;
                }
            }
            result[i] = c;
        }
        return result;
        
    }
}

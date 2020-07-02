import java.util.Scanner;
public class matrixMultiplication 
{
	public static int findMin(int p[])
	{
		//Size of the array
		int n = p.length;
		
		//Array to hold processed values
		int m[][] = new int[n-1][n-1];
		
		//Putting 0s in for singular frames
		for(int i=0; i<n-1; i++)
		{
			m[i][i] = 0;
		}
		
		//Frame size, starting from 2 as multiplication of 1 is always 0
		for(int i=2; i<n; i++)
		{
			for(int j=1; j<n-i+1; j++)
			{
				int l = j+i-1;
				m[j-1][l-1] = Integer.MAX_VALUE;
				for(int k=j; k<l;k++)
				{
					int q = m[j-1][k-1] + m[k][l-1] + (p[j-1]*p[k]*p[l]);
					
					if(q<m[j-1][l-1])
					{
						m[j-1][l-1] = q;
					}
				}
			}
			
		}
		
		return m[0][n-2];
		
	}
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		   
		   int N = sc.nextInt();
		               
			for(int i = 0; i < N; i++)
			{
	            int s = sc.nextInt();
	            
	            int a[] = new int[s];
	            
	            for(int j = 0; j < s; j++)
	            {
	                a[j] = sc.nextInt();
	            }
	            
	            System.out.println(findMin(a));
	        }
		
	}

}

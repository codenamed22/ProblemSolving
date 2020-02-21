import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {

    // Complete the matrixRotation function below.
    static void matrixRotation(List<List<Integer>> matrix, int r) 
    {
        int length = matrix.size();
        int width = matrix.get(0).size();

        int maxRow = matrix.size()-1;
        int maxCol = matrix.get(0).size()-1;
        int row =0;
        int col =0;
        int prev =0;
        int curr =0;
        int rC = 0;  
        while(row<= maxRow && col<= maxCol)
        {
            rC = r%(((length-(2*row))*2)+((width-(2*col)-2)*2));
            //System.out.println(rC);
            while(rC!=0)
            {
                prev = matrix.get(row+1).get(maxCol);

                for(int i=maxCol; i>=row; i--)
                {
                    curr = matrix.get(row).get(i);// a[row, i];
                    matrix.get(row).set(i, prev); //a[row, i] = prev;
                    prev = curr;
                }

                for(int i=row + 1; i<=maxRow; i++)
                {
                    curr = matrix.get(i).get(col); // a[i, col];
                    matrix.get(i).set(col, prev); // a[i, col] = prev;
                    prev = curr;
                }

                for(int i=col + 1; i<=maxCol; i++)
                {
                    curr = matrix.get(maxRow).get(i);// a[maxRow, i];
                    matrix.get(maxRow).set(i, prev); //a[maxRow, i] = prev;
                    prev = curr;
                }

                for(int i=maxRow-1; i>row; i--)
                {
                    curr = matrix.get(i).get(maxCol); //  curr = a[i, maxCol];
                    matrix.get(i).set(maxCol, prev); // a[i, maxCol] = prev;
                    prev = curr;
                }
                rC--;
            }
            row++;
            col++;
            maxCol--;
            maxRow--;
        }

        for(int i=0; i<length; i++)
        {
            for(int j=0; j<width; j++)
            {
                System.out.print(matrix.get(i).get(j)+" ");
            }

            System.out.println();
        }

    }


    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] mnr = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int m = Integer.parseInt(mnr[0]);

        int n = Integer.parseInt(mnr[1]);

        int r = Integer.parseInt(mnr[2]);

        List<List<Integer>> matrix = new ArrayList<>();

        IntStream.range(0, m).forEach(i -> {
            try {
                matrix.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        matrixRotation(matrix, r);

        bufferedReader.close();
    }
}

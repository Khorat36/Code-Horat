A = [2 -1 4;9 6 2;1 3 8];
B = ones(3);
x = [3;6;8];
y = [5 10 15];
disp(A);
disp(B);
disp(x);
c1 = A * B;
C2 = A * x;
C3 = x' * B;
c4 = B * y;
c5 = x * A;
C6 = x * y;
c7 = y * x;
c8 = x * y';
c9 = x .* y;
c10 = A .* B;
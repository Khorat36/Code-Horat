A = [1 1 1;1 2 3;1 3 6];
b = [1; -5; 2];
c = inv(A) * b;
d = A\b;
c1 = det(A);
c2 = rank(A);
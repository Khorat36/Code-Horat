%question one
%A = [2 -1 4;9 6 2;1 3 8];
% B = ones(3);
% x = [3; 6; 8;];
% y = [5 10 15];
% disp(A);
% disp(B);
% disp(x);
% 
% c1= A * B;
% c2= A * x;
% c3= x' * B;
% c4= B * y;
% c5= x * A;
% c6= x * y;
% c7= y * x;
% c8= x * y';
% c9= x .* y;
% c10= A .* B;

%Question 2
% A = [1 1 1;1 2 3;1 3 6];
% b = [1;-5;2];
% c = inv(A) * b;
% d = A\b;
% c1= det(A);
% c2= rank(A);
%Question 3
% A = [1 1;1 2;1 3];
% b = [1;5;10];
% x = A\b;
% c1 = A * x;
%Question 4 
% count = 1;
% i = rand;
% while i <= 20
% i = i + rand;
% count = count + 1;
% end
% disp(count);
%Question 5
xt = @(t) 1 + cos(2*t);
yt= @(t) -1 + sin(4*t);
fplot(xt,yt);
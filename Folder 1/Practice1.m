i = 100;
for l = n:i
n = 0;
die1 = 0;
die2 = 0;
while die1 < 6 || die2 < 6
die1 = randi(6,1);
die2 = randi(6,1); 
n = n + 1;
end
count(l)= i
end

disp(n);
disp(die1);
disp(die2);
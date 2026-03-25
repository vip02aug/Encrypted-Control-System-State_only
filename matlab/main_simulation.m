clear; clc;

A = [0.5 0.0 0.0;
     0.1 0.6 0.0;
     0.0 0.2 0.7];

B = [1.0;
     0.0;
     1.0];

K = [0.2 0.1 0.3];
r = 500.0;

x = [5.0; 2.0; 1.0];

q = 2^31 - 1;
scale = 1.0;
n = size(x,1);
N = 10;

Sx = int64([2 1 0;
            0 1 1;
            1 0 2]);

Vx = int64(zeros(n,1));

disp('Running state-encryption-only simulation...');
disp(' ');

for k = 1:N
    u = controller(K, x, r);
    x_next = system_dynamics(A, B, x, u);

    mx = int64(round(scale * x));
    noise = int64(round(randn(n,1)));

    Vx = state_encrypt(Sx, Vx, mx, noise, q);
    x_rec = state_recover(double(Vx), scale, q);

    fprintf('Step %d\n', k-1);
    disp('x ='); disp(x);
    disp('u ='); disp(u);
    disp('Vx ='); disp(Vx);
    disp('x_rec ='); disp(x_rec);
    disp('----------------------------------------');

    x = x_next;
end

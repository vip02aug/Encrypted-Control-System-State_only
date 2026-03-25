function x_next = system_dynamics(A, B, x, u)
    x_next = A * x + B * u;
end

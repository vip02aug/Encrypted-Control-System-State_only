function u = controller(K, x, r)
    u = r - K * x;
end

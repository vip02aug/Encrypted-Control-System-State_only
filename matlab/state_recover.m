function x_rec = state_recover(Vx, scale, q)
    half_q = floor(q/2);
    x_centered = Vx;

    idx = x_centered > half_q;
    x_centered(idx) = x_centered(idx) - q;

    x_rec = x_centered / scale;
end

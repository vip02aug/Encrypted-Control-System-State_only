function Vx = state_encrypt(Sx, Vprev, mx, noise, q)
    Vx = mod(Sx * Vprev + mx + noise, q);
end

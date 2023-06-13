// run the program 
// start server 
(base) user-2:rust_web_server_concurrent user$ cargo build 
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s

(base) user-2:rust_web_server_concurrent user$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/main`


// start client 

(base) user-2:rust_web_server_concurrent user$ python aiohttp-client-to-rust.py 
time taken: 8.745990152



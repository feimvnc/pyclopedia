# start server 
(base) user-2:rust_web_server_concurrent user$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/main`

# start 01_simple-http.py
# synchronous calls
(base) user-2:client user$ python 01_simple_http_sync.py 
11.093317224


# multiprocessing using multi-cores to run multi processeso
(base) user-2:client user$ python 02_multi_processing_http.py 
2.7904895300000003

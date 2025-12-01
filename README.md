To run this locally, you must download the gguf model from: https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/blob/main/qwen2.5-3b-instruct-q3_k_m.gguf

Once downloaded, place the file in the models folder inside of the tutor file.

### <ins>pip install<ins>
- flask
- llama-cpp-python
- markdown
- requests

### HOW TO RUN
once the above steps are complete, open the command prompt and cd into the project folder.
Then run the following command:
```
python web/app.py
```
Once the command has been executed you should see the following lines of code in your command prompt:
```
Loading GGUF model...
llama_context: n_ctx_per_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
Loading GGUF model...
llama_context: n_ctx_per_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
 * Debugger is active!
 * Debugger PIN: 381-940-800
 ```

 Now you can visit the ai tutor at http://127.0.0.1:5000
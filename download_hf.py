from huggingface_hub import snapshot_download
model_id="meta-llama/Meta-Llama-3-8B-Instruct"
snapshot_download(repo_id=model_id, local_dir="custom_model",
                  local_dir_use_symlinks=False, revision="main")

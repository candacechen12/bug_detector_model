python run.py \
--output_dir=./saved_models \
--tokenizer_name=microsoft/codebert-base \
--model_name_or_path=microsoft/codebert-base \
--do_test \
--train_data_file=../../../dataset/train_scaled.jsonl \
--eval_data_file=../../../dataset/valid_scaled.jsonl \
--test_data_file=../../../dataset/test_scaled.jsonl \
--eval_batch_size 16 \
--block_size 512 \
--max_grad_norm 1.0 \
--seed 123456 \
--train_learning_rate 10e-5 \
--finetune_learning_rate 2e-5 \
--num_train_epochs 40 \
--num_finetune_epochs 5 \
--train_batch_size 32 \
--finetune_batch_size 4 \
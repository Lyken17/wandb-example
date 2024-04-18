TASKs=('boolq' 'piqa' 'social_i_qa' 'hellaswag' 'winogrande' 'ARC-Easy' 'ARC-Challenge' 'openbookqa')
seeds=(42 43 44 45 46 92 93 94 95 96)
MODELs=('NousResearch/Llama-2-7b-hf' 'NousResearch/Llama-2-13b-hf' 'huggyllama/llama-7b' 'huggyllama/llama-13b') 


for model in "${MODELs[@]}"; do
for task in "${TASKs[@]}"; do

python main.py --model $model --dataset $task

done
done
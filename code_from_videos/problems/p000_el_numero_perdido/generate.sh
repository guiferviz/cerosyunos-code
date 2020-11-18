n=1000000
seed=124
python generator.py $n $seed > test/sample_$n.in
cat test/sample_$n.in | python solver.py > test/sample_$n.out

oj generate-input "python generator.py" 20
oj generate-output -c "python solver.py"

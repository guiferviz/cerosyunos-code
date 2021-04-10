RANDOM_SAMPLES = 20
BIG_EXAMPLE =  10000
SEED = 124
TEST_DIR = tests
FILENAME = main


py:
	oj test -c "python $(FILENAME).py" -d $(TEST_DIR)


cpp:
	g++ $(FILENAME).cpp -o $(FILENAME)
	oj test -c "./$(FILENAME)" -d $(TEST_DIR)


clean:
	@echo "Remove random test files"
	rm -f $(TEST_DIR)/random-*
	@echo "Delete binaries"
	rm -f $(FILENAME)


tests: clean
	@echo "Generating test i/o files"
	mkdir -p $(TEST_DIR)
	
	@echo "Generating big example to test efficiency"
	python generator.py $(BIG_EXAMPLE) $(SEED) > $(TEST_DIR)/random-big-$(BIG_EXAMPLE).in
	cat $(TEST_DIR)/random-big-$(BIG_EXAMPLE).in | python solver.py > $(TEST_DIR)/random-big-$(BIG_EXAMPLE).out
	
	@echo "Generating a bunch of random samples"
	oj generate-input "python generator.py" $(RANDOM_SAMPLES) -d $(TEST_DIR)
	oj generate-output -c "python solver.py" -d $(TEST_DIR)

.PHONY: clean, run, ils, ga, ts, cs

# 测试集文件
TEST_FILE = tai100a.dat

clean:
	rm -rf ./pic/*
	find . -type d -name '__pycache__' -exec rm -r {} +

run:
	python3 main.py

ils:
	python3 main.py -a ils -f $(TEST_FILE)

ga:
	python3 main.py -a ga -f $(TEST_FILE)

ts:
	python3 main.py -a ts -f $(TEST_FILE)

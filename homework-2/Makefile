.PHONY: clean
clean:
	rm -f submission/submission.zip submission/model.keras

.PHONY: submit
push: kernel-metadata.json notebooks/*
	kaggle kernels push

.PHONY: submit
status:
	kaggle kernels status tomazmaiasuller/an2dl-hw2-train

.PHONY: pack
pack: submission/submission.zip
	exa -l submission

submission/submission.zip: submission/model.keras submission/model.py
	cd submission; zip -r submission.zip .

# Model Experiment
```
./model_experiment
|---- README.md         // README for instructions, structures
|---- requirements.txt  // dependencies file for environment setup
|---- sources/          // source code for model trainer, predictors
|---- tests/            // test units for `sources`
```

## Getting started

To run the test, please recreate dev environment from `requirements.txt`, then run this script in this directory

```bash
python -m tests.test_sentimentDetector
```
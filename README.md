# dh-hdp-etl-utils

A package to share dh-hdp-etl utils classes and functions between different code bases.

## Updating the package
When the task to update the package has been put up for review, and the changes warrant a new package version, the following has to be done:
- Bump up the package version according to semantic versioning
- Create/update the package tag according to the new version
- Update version in `requirements.txt` in the relevant repositories

### Bump version according to semantic versioning
When changes have been made to the package that warrant a new package version, increment the package version in `pyproject.toml` by changing the `version` value, e.g.:
```
version = "0.1.0"
```

### Create/update package tag
After updating the package version in `pyproject.toml`, the package tag also has to be updated and pushed to the repository.

In the terminal on your IDE in the package repository:
1. List already available tags:
```
git tag -l
```
2. Create new tag if not already present:
```
git tag v0.1.0
```
3. Push tag to repository:
```
git push origin v0.1.0
```
### Update version in `requirements.txt`

After the tag has been created/updated and pushed to the repository, the package version in `requirements.txt` has to be updated for the relevant repositories. For this specific pacakge those are `dh-hdp-federation-api` and `dh-hdp-etl`.

```
pydantic
dhhdpetlutils @ git+https://github.com/MaastrichtUniversity/dh-hdp-etl-utils
pytest
```

Specify a commit hash (2c5d54504a3ece5ed45bb9634a0ed6c5f77cbe98):
```
dhhdpetlutils @ git+https://github.com/MaastrichtUniversity/dh-hdp-etl-utils@2c5d54504a3ece5ed45bb9634a0ed6c5f77cbe98
```

Specify a branch name (e.g. main):
```
dhhdpetlutils @ git+https://github.com/MaastrichtUniversity/dh-hdp-etl-utils@main
```

Specify a tag (e.g. v0.0.1):
```
dhhdpetlutils @ git+https://github.com/MaastrichtUniversity/dh-hdp-etl-utils@v0.0.1
```

## Integrating the package with the IDE
To integrate a package with the IDE to allow for the IDE to find the package and auto-complete package-related code, the package has to be installed (preferably in your virtual environment).
- Install the required package in the correct environment:
```bash
# version tag, specific branch or commit can be used to specify package version, e.g. @DHHDP-789
pip install git+https://github.com/MaastrichtUniversity/dh-hdp-etl-utils@v0.1.0
```
- In case the package has to be uninstalled:
```bash
# using package name
pip uninstall dhhdpetlutils
```

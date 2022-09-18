# Release Process

## Preparation

### Version Bump

Bump the version in [`setup.py`](setup.py) and then open a PR with ths change and land it on
https://github.com/jsirois/p537 master.

## Release

### Push Release Tag

Sync a local branch with https://github.com/jsirois/p537 master and confirm it has the version bump
and changelog update as the tip commit.

Tag the release as `v<version>` and push the tag to https://github.com/jsirois/p537 master:
```
$ git tag --sign -am 'Release 1.0.6' v1.0.6
$ git push --tags https://github.com/jsirois/p537 HEAD:master
```

The release to PyPI is automated from there. You can check on the release action
[here](https://github.com/jsirois/p537/actions?query=workflow%3ARelease).



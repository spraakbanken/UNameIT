# UNameIT

"Universal Names and miscellaneous entities (for) Information Technology"

This repo contains several (open) databases containing information about names (e.g., person names, geographical names, company names, etc).

### Large file storage

This repo uses [Git LFS](https://git-lfs.github.com/) to store large files. To get the files and run the scripts correctly, install Git LFS and then do this inside your clone of the repo:

```sh
git lfs install
git lfs pull
```

### No sensitive information!

Since this repo is not hosted at GU, it is important that we do not store any sensitive information here. Sensitive information are, e.g., any information that can be connected to an individual person.

### Source files

All original database sources should reside in the `src` directory. This is divided into:

- `automatic`: here are databases that are downloaded from other places, or automatically created in some way
- `manual`: here are databases that we build and update manually

Every data source should have a separate directory in `src/automatic` or `src/manual`, and there must be a readme file detailing how the sources have been obtained and what scripts have been used.

### Derived JSON databases

Our preferred result database format is JSON, and they should be automatically created by scripts. The resulting JSON databases should be in the `json` directory.



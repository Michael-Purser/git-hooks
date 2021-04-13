#!/usr/bin/python3


from hook_utils import GitHookExitCode, GitHookLogger

from git import Repo, InvalidGitRepositoryError, NoSuchPathError
from pathlib import PurePosixPath
import sys


def update_submodules(
        repository_path: PurePosixPath,
        logger: GitHookLogger
) -> None:
    try:
        repo = Repo(path=repository_path.as_posix())
    except InvalidGitRepositoryError:
        logger.fail("InvalidGitRepositoryError: There is no git repository at '{}', or the repository is in error"
                    .format(repository_path.as_posix()))
        sys.exit(GitHookExitCode.Failure)
    except NoSuchPathError:
        logger.fail("NoSuchPathError: the specified repository path '{}' does not exist"
                    .format(repository_path.as_posix()))
        sys.exit(GitHookExitCode.Failure)

    if repo.submodules:
        for submodule in repo.submodules:
            logger.info("Updating submodule: '{}'".format(submodule.name))
            submodule.update(recursive=True, init=True)
    else:
        logger.info("No submodules to update")

    logger.success()
    sys.exit(GitHookExitCode.Success)

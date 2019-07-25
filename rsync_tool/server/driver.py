#!/usr/bin/env python3

import FileRepository

repo = FileRepository.FileRepository('/Users/balajipa/Desktop/mp3')
repo.buildFileRepository()
repo.display_repo()

d = repo.get_repo()
print(len(d))

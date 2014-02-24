Deployment is done in the following steps for this project.

1. Bump the revision in setup.py
2. Commit the new revision (git commit -a)
3. Create a new tag from master (git tag <version number from setup.py>)
4. Push changes to github (git push)
5. Push new tag to github (git push --tags)
6. Run the tests in python 2.7 (python setup.py test)
7. Run the tests in python 3 (python3 setup.py test)
8. Push the source and python 2.7 egg to pypi (python setup.py sdist bdist_egg upload)
9. Push the python 3 egg to pypi (python3 setup.py bdist_egg upload)

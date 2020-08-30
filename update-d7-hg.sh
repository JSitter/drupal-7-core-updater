chmod 755 ./d7-updater.py
allparams=${@}
scl enable rh-python35 "./d7-updater.py $allparams"
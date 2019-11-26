#!/bin/bash -e

BASE_URL=http://github.com/intel/compute-runtime/archive/
REPO=${1-$HOME/git/compute-runtime}
function git() { command git -C $REPO "$@"; }

OLDVERSION=`sed -n -e '/^URL/{s,.*'$BASE_URL',,;s,/.*,,p}' Makefile`

git remote update -p
VERSION=`git rev-parse origin/master`
DESCRIPTION=`git describe $VERSION | sed s/-branchpoint-/+/`

if [ "$VERSION" == "$OLDVERSION" ] ; then
	echo "Nothing changed $OLDVERSION == $VERSION"
	exit 0
fi
	

echo "Updating from $OLDVERSION to $VERSION"

echo "PKG_NAME := intel-compute-runtime" > Makefile
echo "URL := $BASE_URL$VERSION/intel-compute-runtime-$DESCRIPTION.tar.gz" >> Makefile
echo "" >> Makefile
echo "" >> Makefile
echo "include ../common/Makefile.common" >> Makefile
${MAKE-make} autospec
#make koji
${Make-make} build
${MAKE-make} repoadd
sleep 60
#cd ..
# take care of rebuilds as per README.clear
#for i in  xf86-video-*; do pushd $i ; git pull ; make bump ; make koji-nowait; popd; done

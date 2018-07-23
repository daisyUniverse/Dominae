#!/bin/bash
cd ~/.dominae/VOX/
sox `xargs -a ~/.dominae/VOX/voxfn.txt`
echo $?
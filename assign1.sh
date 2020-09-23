#!/bin/sh

echo "====START===="
sh ./neighbor-districts-modified.sh
echo "1. neighbor-districts-modified.sh Done"
sh ./case-generator.sh
echo "2. case-generator.sh Done"
sh ./edge-generator.sh
echo "3. edge-generator.sh Done"
sh ./neighbor-generator.sh
echo "4. neighbor-generator.sh Done"
sh ./state-generator.sh
echo "5. state-generator.sh Done"
sh ./zscore-generator.sh
echo "6. zscore-generator.sh Done"
sh ./method-spot-generator.sh
echo "7. method-spot-generator.sh Done"
sh ./top-generator.sh
echo "8. top-generator.sh Done"
echo "====END===="

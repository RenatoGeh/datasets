package main

import (
	"github.com/RenatoGeh/gospn/io"
	"os"
	"path/filepath"
)

func main() {
	path := os.Args[1]
	cmn, _ := filepath.Abs(path)
	io.BufferedPGMFToData(cmn, "all.data")
}

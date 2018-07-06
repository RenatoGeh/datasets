package main

import (
	"fmt"
	mnist "github.com/petar/GoMNIST"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Printf("Usage: %s n [test|train] bits debug\n"+
			"n     - number of digits to convert\n"+
			"test  - use test set\n"+
			"train - use training set\n"+
			"bits  - downscale resolution to bits number of bits\n"+
			"debug - whether to sample digits (saves to /tmp/); 1 yes, 0 no\n", os.Args[0])
		os.Exit(1)
	}
	max := 256
	debug := false
	if len(os.Args) >= 4 {
		b, e := strconv.ParseUint(os.Args[3], 10, 8)
		if e != nil {
			fmt.Println(e)
			panic(e)
		}
		max = 1 << b
	}
	if len(os.Args) >= 5 {
		b, e := strconv.ParseUint(os.Args[4], 2, 1)
		if e != nil {
			fmt.Println(e)
			panic(e)
		}
		if b == 1 {
			debug = true
		}
	}
	n, e := strconv.Atoi(os.Args[1])
	if e != nil {
		fmt.Println(e)
		panic(e)
	}
	u := os.Args[2]

	fmt.Println("Extracting...")
	train, test, err := mnist.Load("./original")
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
	var D *mnist.Set
	var name string
	if u == "test" {
		D = test
		name = fmt.Sprintf("compiled/test_%d_%d.data", max, n)
	} else {
		D = train
		name = fmt.Sprintf("compiled/train_%d_%d.data", max, n)
	}

	w, h := mnist.Width, mnist.Height
	t := w * h

	f, e := os.Create(name)
	defer f.Close()
	if e != nil {
		fmt.Println(err)
		panic(err)
	}

	for i := 0; i < t; i++ {
		fmt.Fprintf(f, "var %d %d\n", i, max)
	}
	fmt.Fprintf(f, "var %d 10\n", t)

	m := int((n-1)/10) + 1
	L := make([]int, 10)
	k := 0

	n = len(D.Images)
	for i := 0; ; i++ {
		if i >= n {
			i = i % n
		}
		image, label := D.Images[i], D.Labels[i]
		if L[label] >= m {
			last := k
			k |= (1 << label)
			if k != last {
				fmt.Println(k, label)
			}
			if k == (1<<10)-1 {
				break
			}
			continue
		}
		L[label]++
		var s *os.File
		if debug {
			s, _ = os.Create(fmt.Sprintf("/tmp/%s_%d_%d.pgm", u, i, label))
			fmt.Fprintf(s, "P2\n%d %d\n%d\n", w, h, max-1)
		}
		for j := range image {
			p := int(image[j])
			p = ((max - 1) * p) / 255
			fmt.Fprintf(f, "%d ", p)
			if debug {
				fmt.Fprintf(s, "%d ", p)
			}
		}
		fmt.Fprintf(f, "%d\n", label)
		if debug {
			s.Close()
		}
	}

	fmt.Println("Done.")
}

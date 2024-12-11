package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type cacheResult struct {
	v    int64
	iter int
}

var cache = make(map[cacheResult]int64)

func main() {
	b, err := os.ReadFile("input1.txt")
	if err != nil {
		panic(err)
	}
	values := []int64{}
	for _, s := range strings.Fields(string(b)) {
		v, err := strconv.ParseInt(s, 10, 64)
		if err != nil {
			panic(err)
		}
		values = append(values, v)
	}

	total := int64(0)
	for _, v := range values {
		total += process(v, 75)
	}

	fmt.Println(total)
}

func process(value int64, iteration int) int64 {
	if v, ok := cache[cacheResult{v: value, iter: iteration}]; ok {
		return v
	}

	if iteration == 0 {
		return 1
	}

	if value == 0 {
		ret := process(1, iteration-1)
		cache[cacheResult{v: value, iter: iteration}] = ret
		return ret
	}

	if int(math.Log10(float64(value))+1)%2 == 0 {
		str_value := fmt.Sprintf("%d", value)
		midPoint := len(str_value) / 2
		left, err := strconv.ParseInt(str_value[0:midPoint], 10, 64)
		if err != nil {
			panic(err)
		}
		right, err := strconv.ParseInt(str_value[midPoint:], 10, 64)
		if err != nil {
			panic(err)
		}
		t := int64(0)
		t += process(left, iteration-1)
		t += process(right, iteration-1)
		cache[cacheResult{v: value, iter: iteration}] = t
		return t
	}

	r3 := process(value*2024, iteration-1)
	cache[cacheResult{v: value, iter: iteration}] = r3
	return r3
}

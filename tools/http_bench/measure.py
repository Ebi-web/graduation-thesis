package main

import (
	"crypto/tls"
	"flag"
	"fmt"
	"io/ioutil"
	"net/http"
	"time"

	"github.com/quic-go/quic-go/http3"
)

func main() {
	// コマンドラインオプションの定義と解析
	http1 := flag.Bool("http1.1", false, "Use HTTP/1.1")
	http2 := flag.Bool("http2", false, "Use HTTP/2")
	http3Flag := flag.Bool("http3", false, "Use HTTP/3")
	flag.Parse()

	// オプションの確認
	if (*http1 && *http2) || (*http2 && *http3Flag) || (*http1 && *http3Flag) || (!*http1 && !*http2 && !*http3Flag) {
		fmt.Println("Error: Specify exactly one of --http1.1, --http2, or --http3")
		return
	}

	// HTTPバージョンに基づいてクライアントを設定
	var client *http.Client
	if *http1 {
		client = &http.Client{}
	} else if *http2 {
		client = &http.Client{
			Transport: &http.Transport{
				TLSClientConfig:   &tls.Config{InsecureSkipVerify: true},
				ForceAttemptHTTP2: true,
			},
		}
	} else if *http3Flag {
		client = &http.Client{
			Transport: &http3.RoundTripper{
				TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
			},
		}
	}

	urls := []string{
		"http://localhost:8081", // ここにHTTP/1.1 URLを置き換えてください
		//"https://example.com", // ここにHTTP/2 URLを置き換えてください
		//"https://example.com", // ここにHTTP/3 URLを置き換えてください
	}

	for _, url := range urls {
		measurePerformance(client, url)
	}
}

func measurePerformance(client *http.Client, url string) {
	start := time.Now()
	resp, err := client.Get(url)
	if err != nil {
		fmt.Printf("Failed to GET from %s: %v\n", url, err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Failed to read response body from %s: %v\n", url, err)
		return
	}

	elapsed := time.Since(start)
	dataSize := len(body)
	fmt.Printf("URL: %s\n", url)
	fmt.Printf("Time taken: %v\n", elapsed)
	fmt.Printf("Data size: %d bytes\n", dataSize)
	fmt.Printf("Throughput: %f bytes/sec\n", float64(dataSize)/elapsed.Seconds())
}

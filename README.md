# Playwrightでフルスクリーンショットを撮る #

## Note

※本ソフトウェアの実行及び動作結果に関しまして、  
　動作を必ず保証するものではなく、発生した結果等について一切の責任を負いません。

## Summary

[Playwright](https://playwright.dev/) を使ってWebページのフルスクリーンキャプチャを取得します。

## Playwright

https://playwright.dev/

## Files

```bash

```

## Setup & Build docker image

```bash
https://github.com/sakasa/playwright-screenshot-sample.git
cd playwright-screenshot-sample/
docker build -t pw-local:0.0.1 .
```

## Usage

```bash
docker container run --rm -it [-v "$(pwd)/work"] pw-local:0.0.1 https://google.com
```
- ローカルでプログラムを変更しながら実行したい場合は `-v` オプションを付けてください。
- 末尾のURLは複数指定可能です。スペース区切りで複数渡してください。（スリープなど入れていないので同じサイトの複数画面で実行する場合などは気をつけてください）

## Outputs

- Image(png)
  - screenshot/{URL(replace slash->underscore)}_screenshot_{%Y%m%d%H%M}.png
    - ex. screenshot/https__google.com_screenshot_202304201234.png
- PDF
  - screenshot/{URL(replace slash->underscore)}_page_{%Y%m%d%H%M}.pdf
    - ex. screenshot/https__google.com_page_202304201234.pdf

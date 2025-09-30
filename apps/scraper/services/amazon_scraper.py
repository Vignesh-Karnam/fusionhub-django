import re

import requests
from selectolax.parser import HTMLParser


class AmazonScraper:
    def fetch_product(self, asin):
        url = f"https://www.amazon.in/dp/{asin}"
        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'device-memory': '8',
            'downlink': '10',
            'dpr': '1.5',
            'ect': '4g',
            'priority': 'u=0, i',
            'referer': f'https://www.amazon.in/s?k={asin}',
            'rtt': '50',
            'sec-ch-device-memory': '8',
            'sec-ch-dpr': '1.5',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-ch-viewport-width': '885',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'viewport-width': '885',
            'Cookie': 'session-id=257-9177516-2834731; i18n-prefs=INR; lc-acbin=en_IN; ubid-acbin=257-0026991-0189330; at-acbin=Atza|IwEBII-eh7yPGXTzbJcYZI58-x_8nApNMS1lMazo9-Jf8wrPYBm1UPr1CY-p2HgAFvn24WbaDK7eFX5-ZKSezKsvGHWUEoAAqdoa2rDPU0t2OYmrBbC_sh4RUwQHTvw_l4lDP527Vxp3X6HbJsXCs8uvZm5UZ6lrwH0XJDoiQw3bni3zCOECSCrOl1TeUBefEBbUfsO812CXNNXlweSPWR67W_xESKUv-IM2fAdDd1Kb37oxfwc9WNxYruXZp-T1aZEpRtU; sess-at-acbin="wtTb0f3dvr/CwRHET/NSEF403zqdAG8dBQ7hVOo2uJo="; sst-acbin=Sst1|PQHdcRCwQlyRG6xQa7STEGPzCXv7A-1hBCiZ0OY7kzMfbYMRBJpDtlQAFOEny54x86mNLH6fnRd_0KnaBgKyx1nDQ0cPibIOVZB-_t5TGdgOzyKK8XDs0zj2PlhDL2nA4i3fp_mo6X4ovfUcHdC7ragFRxjylB5hUu7x1-H7Y38uzcoJSuXtPm5oYnCS8AMmWMnEt8hqDxp543GyXQy2jCSl4VfTL0eSFYpyzQ3nDbw7r_PaZr8FAopoO3C2RchJLStjw0CQj6M2V01tY1z17NeUfsg6fwel4BLYVR9R5RQ3I1g; session-id-time=2082787201l; csm-hit=tb:5WGJ9CGK844S6GDSJC5M+s-DHBMR7WGKDBZFNRF2RZ2|1758822807898&t:1758822807898&adb:adblk_no; session-token=0xr4ddZViSCugc7qrNr8tflVtdlg/XAI+YfYjICi7A61KYwHCcSoEho8sKhNiE765BtIwg5VEVRqtST+QzTsyyTKn0FvPnI8hi9ZiE7WtPI0rDrfmMPUk/Zjl0OOln6Ju0THw7TM4zvrwZEHOiCcrXPCmD/AT1WoezsIXyNb5UdKLeEIUaNdYX/p1zbfg98B+U5XVzqrlL3kdMEHOjPvvQhEK3CJ673m8hpqYJd1oDP1MtyTwczSy24N7PVY2JuFaNs+wjnaFImIzJVkLGNvZ5T7Bhd2PYsDm4z1U4ntsb/So8yw39BbmPVs0at3Ne/GSv9gWXK8cJGjw5qEauu1swVm+2FMAsIlPQtM5Mtn0gxgq/pgkXUH0IOZ/Dyu1uQJ; x-acbin="7ZZ9S6LWmLC?PL2ePQkwAEgjDV634DDdutwmkRgrDnjxWsM91jkpi^@?qxjMYFIbD"; rxc=AGLinokRSD4NOg2F3TI; session-token=XSCQDy+e5FzHgbk9G0+0BtA6ubikC5Sp7lNTjpTPdejGy0JcM36BICEhGLZ10dJpX8gbvIDAM4mI8gDCdi3Mp4SiF9Pu+fofnMXaD8wDXv9GmmQ8vDAGTAZlu6aWH2h9DYmVMsxD8CrRTbSQ24NlV/G09ogSzIW8fPmIW5AOkyWpqAdyLZyA7Ss72PvkD3poqJqnTdezZeOL9a02ARfhj03r7neN121dtkl+p8KXcnZe85vRI8FeR1m4zgJTdkch+rrX1FrT4E5hJz+ZXnIG9/rQxwyoNz9bz4iIz++8PLAKPwjdluKyxMBuQbwKrOBbcXvcn7spk4jr/gHfrDPu0Ej4g1Ut2joL'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            tree = HTMLParser(response.text)
            title = tree.css_first('#titleSection').text().strip()
            price = tree.css_first('#corePriceDisplay_desktop_feature_div')
            selling_price = price.css_first('.a-price-whole').text()
            # discount = price.css_first('.a-size-large.a-color-price.savingPriceOverride.aok-align-center.reinventPriceSavingsPercentageMargin.savingsPercentage').text().replace('%', '').replace('-', '')
            # mrp = tree.css_first('[class="a-price a-text-price"] > [class="a-offscreen"]').text().replace('₹', '').replace(',', '')
            category = tree.css_first('#wayfinding-breadcrumbs_feature_div').text()
            product_overview_text = tree.css_first('#productOverview_feature_div').css_first('table').text()
            match = re.search(r"Brand\s+([^\s].*?)\s{2,}", product_overview_text)
            if match:
                brand = match.group(1).strip()
            else:
                brand = None
            return {
                "product_id": asin,
                "title": title,
                "brand": brand,
                "category": category,
                # "mrp": mrp,
                "selling_price": selling_price,
                # "discount": discount
            }
        return {"asin": asin, "error": response.status_code}

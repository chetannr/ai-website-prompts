#!/usr/bin/env python3
"""
Extract content and images from the original Law Park Educational Trust website.
"""

import os
import json
import requests
from pathlib import Path
from urllib.parse import urlparse

# Website content extracted from browser
WEBSITE_CONTENT = {
    "mission": {
        "tagline": "Making Bleak Futures, Brighter",
        "description": "Law Park Educational Trust helps children from rural areas across India get their right to education through partially funded scholarships.",
        "statistic": "35 Million+ Children In India Between The Age Of 6-14 Do Not Go To School"
    },
    "about": {
        "title": "When It Comes To Education, No Child Deserves To Be Left Behind",
        "description": "We Law Park Education Trust (LPET) are on a mission to give deserving children a chance at a better future by allowing them to discover their potential and become contributing members of society.",
        "quote": "From Little Seeds grows mighty trees"
    },
    "impact": {
        "points": [
            "We put underprivileged children in classrooms and give them their right to education and their risks of exploitation through child labour. They eventually become confident enough to face their life.",
            "We educate the girl child and play a part in ensuring that they do not become victims of child marriage.",
            "We create a future generation of bright talent that adds value to society and takes part in imparting positive changes in their communities."
        ],
        "statistics": {
            "years": "10+ Years Of Giving children access to education",
            "students": "200+ students supported and counting (from 2016 to till date)",
            "villages": "50+ Villages with 4 south Indian states",
            "donors": "100+ Donors"
        }
    },
    "trustees": [
        {
            "name": "Mrs. Charulatha",
            "role": "Managing Trustee",
            "bio": "Mrs. Charulatha, Founder of Law Park Educational Trust, during her young age used to teach poor children in her locality free of cost. That was the foundation to start this Educational Trust in the name of Law Park Educational Trust. She did her B.A Economics, Chennai and did her L.LB., at Bangalore and completed with PGDIPRL in National Law School of India, University, Bangalore. Mrs. Charulatha, always encouraged children to study and many times she would pay fees to those children even before she started this Trust. Most of the times she is surrounded with children asking doubts in their studies which continued even today."
        },
        {
            "name": "MR. S.M. MANJUNATHA",
            "role": "Trustee",
            "bio": "Hailing from the small and beautiful village name Sadenahalli in Karnataka and a Trustee of Law Park Educational Trust. Since childhood, he had always had a passion for inspiring the poor and so, he was the first member of his family to leave the village he was born and raised in to study in the city. He graduted with a degree in Law from Bangalore and encouraged his fellow friends and cousins to follow in his footsteps and also graduate. Moreover, he funded many children from his village who have now grown into well settled, contributing members of society."
        }
    ],
    "process": {
        "title": "How We Advance Our Mission",
        "steps": [
            {
                "title": "Identify",
                "description": "School principals, well-wishers, and citizens of communities nominate deserving students from income deprived backgrounds who need financial support to continue their education."
            },
            {
                "title": "Validate",
                "description": "We visit to location, gather the students with parents in one place and interview each student nomined and their parents to verify the genuineness of their case and help them financially for their education."
            },
            {
                "title": "Embrace",
                "description": "We take the children under our folds and pay up to 75% of their tuition fees at their current school. The parents will cover the remaining part of the tuition fees to ensure their involvement in educating their children. We believe that anything given for fully free will have no value."
            },
            {
                "title": "Incubate",
                "description": "Our team will pay the school fees directly to the school rather than giving them to the parents to prevent misappropriation of the funds. As a result, students can focus solely on their studies without constantly worrying about finances, tap into their fullest potential and thrive throughout their academic careers."
            }
        ]
    },
    "testimonials": [
        {
            "text": "I'm impressed with the dedication & focus in bringing back the children to school, I echo their thoughts & approach in short listing each student to ensure their success is unparalleled. Appreciate this CSR initiative from Law Park Educational Trust!!",
            "author": "Sreekanth",
            "role": "Director, Tech Hat Pvt., Ltd."
        },
        {
            "text": "We have known Law Park Educational Trust for few years. It is a genuine and selfless effort of the Trustees to provide financial and other educational resources to children in need with the main goal of right to education regardless of socioeconomic background.",
            "author": "Dr. Varalakshmi and Dr. Nandakumar",
            "role": "Hershey, USA"
        },
        {
            "text": "Law Park Education Trust is doing a phenomenal work by facilitating the provision of basic right of education to the underprivileged children of our society and country at large.",
            "author": "Aishwarya K",
            "role": "Director, Versalis International"
        }
    ],
    "contact": {
        "phone": "+91-9945665379",
        "email": "empower@lawparkeducationaltrust.org"
    }
}

# Image URLs from the website
IMAGE_URLS = {
    "logo": "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1712312035397lawparkeducationaltrustonlylogo.png",
    "homepage_hero": "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685527116208cuteindianfarmerchildstudyingwithhisfatherhomescaled.jpeg",
    "homepage_images": [
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685533437292istockphoto1097817298170667a.jpeg",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685533434260photo1582886986183f8d30e8a1ac3.jpeg",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685533431325istockphoto1163984047170667a.jpeg"
    ],
    "about_images": [
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685522521637educationiskeytoresolveallissues.jpeg",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685533195276biharindiafebruary152016unidentifiedchilderngoschool1.jpeg"
    ],
    "gallery_images": [
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685615031850Screenshot13.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685615024990Screenshot17.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685615016480Screenshot18.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685615008941Screenshot15.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685615001984Screenshot16.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614995721Screenshot19.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614989987Screenshot65.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614982927Screenshot66.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614978248Screenshot62.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614973424Screenshot60.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614968252Screenshot28.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614962209Screenshot26.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614956359Screenshot29.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614948974Screenshot23.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614940919Screenshot20.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614935442Screenshot25.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614924111Screenshot24.png",
        "https://dce8a5e5981c702a93be-995a5d988a36b22304388b702a0355a7.ssl.cf1.rackcdn.com/1685614914552Screenshot30.png"
    ]
}

def download_image(url, output_path):
    """Download an image from URL."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def main():
    """Main extraction function."""
    script_dir = Path(__file__).parent
    website_dir = script_dir / "website" / "public" / "website_content"
    website_dir.mkdir(parents=True, exist_ok=True)
    
    images_dir = website_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    
    print("Downloading images from original website...")
    
    # Download logo
    logo_path = images_dir / "logo.png"
    if download_image(IMAGE_URLS["logo"], logo_path):
        print(f"✓ Downloaded logo: {logo_path.name}")
    
    # Download homepage images
    for i, url in enumerate(IMAGE_URLS["homepage_images"]):
        ext = url.split('.')[-1]
        filename = f"homepage_{i+1}.{ext}"
        path = images_dir / filename
        if download_image(url, path):
            print(f"✓ Downloaded: {filename}")
    
    # Download about images
    for i, url in enumerate(IMAGE_URLS["about_images"]):
        ext = url.split('.')[-1]
        filename = f"about_{i+1}.{ext}"
        path = images_dir / filename
        if download_image(url, path):
            print(f"✓ Downloaded: {filename}")
    
    # Download gallery images (limit to first 10 for now)
    for i, url in enumerate(IMAGE_URLS["gallery_images"][:10]):
        ext = url.split('.')[-1]
        filename = f"gallery_{i+1}.{ext}"
        path = images_dir / filename
        if download_image(url, path):
            print(f"✓ Downloaded: {filename}")
    
    # Save content as JSON
    content_path = website_dir / "website_content.json"
    with open(content_path, 'w', encoding='utf-8') as f:
        json.dump(WEBSITE_CONTENT, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Content saved to: {content_path}")
    print(f"✓ Images saved to: {images_dir}")
    print("\nExtraction complete!")

if __name__ == "__main__":
    main()


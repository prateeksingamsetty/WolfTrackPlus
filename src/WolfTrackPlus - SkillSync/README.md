# SkillSync

SkillSync has been seamlessly integrated into the robust open-source resume builder and parser, WolfTrackPlus.

The objective of SkillSync is to offer complimentary access to contemporary and professionally designed resume templates, empowering individuals to confidently apply for jobs.

## ⚒️ SkillSync - Resume Builder

SkillSync's resume builder facilitates the effortless creation of a contemporary and polished professional resume for users.

### Motivation 

A Resume Builder application proves essential for individuals navigating the competitive realm of job applications. By simplifying the process of creating professional documents, this application streamlines the often challenging task. Its user-friendly interface guides individuals through different sections, providing various templates and formatting options for a polished presentation. Customized content suggestions, based on industry or career level, enhance personalization, while real-time feedback aids users in refining their resumes on the fly. The advantage of anytime, anywhere access adds to its convenience. Integration with job portals ensures smooth application submissions, and the application's potential to offer learning resources and analytics guarantees ongoing improvement. Essentially, a well-crafted Resume Builder not only optimizes the efficiency of resume creation but also significantly contributes to users' overall career development by delivering a comprehensive and user-friendly experience.

It has 5 Core Features:

| <div style="width:285px">**Feature**</div> | **Description** |
|---|---|
| **1. Real Time UI Update** | The resume PDF updates in real time as you input information, allowing for an easy preview of the final output. |
| **2. Modern Professional Resume Design** | The resume PDF follows modern professional design practices, adhering to U.S. best practices and ATS-friendly standards for platforms like Greenhouse and Lever. It automatically adjusts fonts, sizes, margins, and bullet points to ensure consistency and prevent errors. |
| **3. Privacy Focus** | The app operates solely on your browser, requiring no sign-up, and ensures data never leaves your browser, providing peace of mind regarding personal data. (Interesting fact: The app functions even offline.) |
| **4. Import From Existing Resume PDF** | Users can import an existing resume PDF directly, enabling a quick update to a modern professional design within seconds. |
| **5. Successful Track Record** | OpenResume users have successfully secured interviews and job offers from prominent companies like Dropbox, Google, Meta, showcasing its effectiveness and endorsement by recruiters and hiring managers. |

## 🔍 SkillSync - Resume Parser

The second element of SkillSync is the resume parser. For individuals with an already established resume, this feature aids in evaluating and verifying its compatibility with Applicant Tracking Systems (ATS).

## 📚 Tech Stack

| <div style="width:140px">**Category**</div> | <div style="width:100px">**Choice**</div> | **Descriptions** |
|---|---|---|
| **Language** | [TypeScript](https://github.com/microsoft/TypeScript) | TypeScript is JavaScript with static type checking and helps catch many silly bugs at code time. |
| **UI Library** | [React](https://github.com/facebook/react) | React’s declarative syntax and component-based architecture make it simple to develop reactive reusable components. |
| **State Management** | [Redux Toolkit](https://github.com/reduxjs/redux-toolkit) | Redux toolkit reduces the boilerplate to set up and update a central redux store, which is used in managing the complex resume state. |
| **CSS Framework** | [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss) | Tailwind speeds up development by providing helpful css utilities and removing the need to context switch between tsx and css files. |
| **Web Framework** | [NextJS 13](https://github.com/vercel/next.js) | Next.js supports static site generation and helps build efficient React webpages that support SEO. |
| **PDF Reader** | [PDF.js](https://github.com/mozilla/pdf.js) | PDF.js reads content from PDF files and is used by the resume parser at its first step to read a resume PDF’s content. |
| **PDF Renderer** | [React-pdf](https://github.com/diegomura/react-pdf) | React-pdf creates PDF files and is used by the resume builder to create a downloadable PDF file. |

## 📁 SkillSync Feature Structure

SkillSync is created with the NextJS web framework and follows its project structure. The source code can be found in `src/app`. There are a total of 4 page routes as shown in the table below. (Code path is relative to `src/app`)

| <div style="width:115px">**Page Route**</div> | **Code Path** | **Description** |
|---|---|---|
| / | /page.tsx | Home page that contains hero, auto typing resume, steps, logo cloud, etc |
| /resume-import | /resume-import/page.tsx | Resume import page, where you can choose to import data from an existing resume PDF. The main component used is `ResumeDropzone` (`/components/ResumeDropzone.tsx`) |
| /resume-builder | /resume-builder/page.tsx | Resume builder page to build and download a resume PDF. The main components used are `ResumeForm` (`/components/ResumeForm`) and `Resume` (`/components/Resume`) |
| /resume-parser | /resume-parser/page.tsx | Resume parser page to test a resume’s AST readability. The main library util used is `parseResumeFromPdf` (`/lib/parse-resume-from-pdf`) |

## 💻 Local Development for standalone SkillSync Application

### Method 1: npm

1. Download the repo
2. Change the directory `cd skill-sync`
3. Install the dependency `npm install`
4. Start a development server `npm run dev`
5. Open your browser and visit [http://localhost:3000](http://localhost:3000) to see SkillSync live

### Method 2: Docker

1. Download the repo
2. Change the directory `cd skill-sync`
3. Build the container `docker build -t skill-sync .`
4. Start the container `docker run -p 3000:3000 skill-sync`
5. Open your browser and visit [http://localhost:3000](http://localhost:3000) to see SkillSync live

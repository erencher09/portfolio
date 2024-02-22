// src/components/Projects.js

import { CodeIcon } from "@heroicons/react/solid";
import React from "react";
import { projects } from "../data";

export default function Projects() {
  return (
    <section id="projects" className="text-gray-200 bg-gradient-to-r from-gray-900 to-blue-600 body-font">
      <div className="container px-5 py-10 mx-auto text-center lg:px-40">
        <div className="flex flex-col w-full mb-20">
          <CodeIcon className="mx-auto inline-block w-10 mb-4" />
          <h1 className="sm:text-4xl text-3xl font-medium title-font mb-4 text-white">
            Products I've Built
          </h1>
          <p className="lg:w-3/3 mx-auto leading-relaxed text-left">
          I'm an experienced DevOps Engineer with expertise in AWS, specializing in building scalable cloud infrastructure 
          for SaaS ERP applications. My proficiency in release management and automation allows me to
          enhance release coordination and CI/CD pipeline efficiency. 
          As a certified Scrum Master, I excel in leading agile teams, 
          driving productivity and fostering innovation. I'm committed to delivering high-quality solutions, 
          streamlining operations, and ensuring customer satisfaction.

          </p>
        </div>
        <div className="flex flex-wrap -m-4">
          {projects.map((project) => (
            <a
              href={project.link}
              key={project.image}
              className="sm:w-1/2 w-100 p-4">
              <div className="flex relative">
                <div className="px-8 py-10 relative z-10 w-full border-4 border-gray-800 bg-gray-900 opacity-100">
                  <h2 className="tracking-widest text-sm title-font font-medium text-blue-600 mb-1">
                    {project.subtitle}
                  </h2>
                  <h1 className="title-font text-lg font-medium text-white mb-3">
                    {project.title}
                  </h1>
                  <p className="leading-relaxed">{project.description}</p>
                </div>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
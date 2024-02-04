import tkinter as tk
from tkinter import ttk
import TKinterModernThemes as TKMT
from library.AppEvent import AppEvent, AppEventType
from managers.EventManager import EventManager
from controller.RecordingController import RecordingController

class TitleView(tk.Frame):
   
    def __init__(self, eventManager: EventManager, recordingController: RecordingController, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.eventManager = eventManager
        self.recordingController = recordingController

        self.videoTitle = tk.StringVar(value="")
        self.annotationPath = tk.StringVar(value="")

        self.videoURL = tk.StringVar(value="")
        self.videoTitle = tk.StringVar(value="")
        self.annotationPath = tk.StringVar(value="")
        # self.videoTitle.trace_add('write', self.videoURLUpdated)
        self.parent = None
    
    def render(self, parent: TKMT.WidgetFrame):
        self.parent= parent
        # self.parent.Text("Title View")
        self.parent.setActiveCol(0)
        # self.titleFrame = self.parent.addLabelFrame("Title View", padx=(0,1), pady=(0,1))
        newProjButton = self.parent.Button(text="Add new project", command=self.renderNewProjectView)
        newProjButton.grid(row=0, column=0, padx=10, pady=10)
        saveProjButton = self.parent.Button(text="Save project", command=self.saveProject)
        saveProjButton.grid(row=0, column=1, padx=10, pady=10)
        recordingName = self.parent.Text(text="Recording Name: " + self.recordingController._recording.name)
        recordingName.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        annotationPathLabel = self.parent.Text(text="Annotation Path: " + self.recordingController._recording.annotation_path)
        # annotationPathLabel = self.parent.Text(text="Annotation Path: " + self.recordingController._recording.annotation_path, widgetkwargs={"textvariable":self.annotationPath})
        annotationPathLabel.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        videoPath = self.parent.Text(text="Video Path: " + self.recordingController._recording.video_path)
        videoPath.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def saveProject(self):
        self.eventManager.onEvent(AppEvent(type=AppEventType.saveProject, data={}))

    def renderNewProjectView(self):
        window = NewProjectWindow(self, "park", "dark")
        window.run()
    
    def initiateNewProject(self, videoURL: str, videoTitle: str, annotationPath: str):
        self.videoURL.set(videoURL)
        self.videoTitle.set(videoTitle)
        self.annotationPath.set(annotationPath)

        # delay so that the new project window can close.
        self.after(1000, self.loadNewProject)
    
    def loadNewProject(self):
        self.eventManager.onEvent(AppEvent(
            type=AppEventType.newProject, 
            data={
                    "videoURL": self.videoURL.get(),
                    "videoTitle": self.videoTitle.get(),
                    "annotationPath": self.annotationPath.get()
                }
            ))


    
class NewProjectWindow(TKMT.ThemedTKinterFrame):
    def __init__(self, titleView: TitleView, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__("TITLE", theme, mode, usecommandlineargs, usethemeconfigfile)
        self.titleView = titleView

        self.newVideoTitle = tk.StringVar(value="")
        self.newVideoURL = tk.StringVar(value="")
        self.newVideoAnnotationPath = tk.StringVar(value="")
        
        self.setActiveCol(0)
        # self.startFrame = self.parent.addLabelFrame("Start", padx=(0,1), pady=(0,1))
        self.urlFrame = self.addLabelFrame("Video URL")
        self.urlFrame.Entry(self.newVideoURL, widgetkwargs={"width": 80})
        self.titleFrame = self.addLabelFrame("Title")
        self.titleFrame.Entry(self.newVideoTitle, widgetkwargs={"width": 80})
        self.annotationPathFrame = self.addLabelFrame("Annotation Path")
        self.annotationPathFrame.Entry(self.newVideoAnnotationPath, widgetkwargs={"width": 80})
        self.Button("Save", self.save)
        self.Button("Cancel", self.cancel)

    
    def save(self):
        # print("newVideoAnnotationPath", self.newVideoAnnotationPath.get())
        # print("newVideoTitle", self.newVideoTitle.get())
        self.titleView.initiateNewProject(videoURL=self.newVideoURL.get(), videoTitle=self.newVideoTitle.get(), annotationPath=self.newVideoAnnotationPath.get())
        self.root.destroy()
    
    def cancel(self):
        self.root.destroy()

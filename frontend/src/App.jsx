import { useState } from "react";
import SideBar from "./components/SideBar";
import ChatPage from "./components/ChatPage";
import "./App.css"

function App() {
  return (
    <div className="mainpage">
      <SideBar></SideBar>
      <ChatPage></ChatPage>
    </div>
  )
}


export default App;
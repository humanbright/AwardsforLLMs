'use client'

import React, {useState, useRef, useEffect} from 'react'
import {v4 as uuidv4} from 'uuid'

export default function Chat() {
  const [messages, setMessages] = useState([])
  const [inputMessage, setInputMessage] = useState('')
  const messagesEndRef = useRef(null)
  const [socket, setSocket] = useState(null)
  const clientId = useRef(uuidv4())

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({behavior: 'smooth'})
  }

  useEffect(() => {
    const newSocket = new WebSocket(
      `wss://fitting-correctly-lioness.ngrok-free.app/ws?client_id=${clientId.current}`,
    )

    newSocket.onopen = () => {
      console.log('WebSocket connection established')
    }

    newSocket.onmessage = (event) => {
      const data = JSON.parse(event.data)
      console.log(data)
      if (data.event === 'chat') {
        setMessages((prevMessages) => [
          ...prevMessages,
          {role: 'assistant', content: data.content},
        ])
      }
    }

    newSocket.onclose = () => {
      console.log('WebSocket connection closed')
    }

    setSocket(newSocket)

    return () => {
      newSocket.close()
    }
  }, [])

  useEffect(scrollToBottom, [messages])

  const handleSendMessage = () => {
    if (inputMessage.trim() !== '' && socket) {
      const newMessage = {role: 'user', content: inputMessage}
      setMessages((prevMessages) => [...prevMessages, newMessage])
      socket.send(
        JSON.stringify({
          event: 'chat',
          messages: [...messages, newMessage],
        }),
      )
      setInputMessage('')
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSendMessage()
    }
  }

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <div className="flex-1 overflow-y-auto p-6 max-w-4xl mx-auto w-full">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`mb-4 ${
              message.role === 'user'
                ? 'flex justify-end'
                : 'flex justify-start'
            }`}
          >
            <div
              className={`max-w-xs md:max-w-md lg:max-w-lg xl:max-w-xl p-3 rounded-lg ${
                message.role === 'user'
                  ? 'bg-blue-500 text-white'
                  : 'bg-white text-gray-800 shadow-md'
              }`}
            >
              {message.content}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div className="p-4 bg-white border-t">
        <div className="flex max-w-4xl mx-auto">
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            className="flex-1 border rounded-l-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Type a message..."
          />
          <button
            onClick={handleSendMessage}
            className="bg-blue-500 hover:bg-blue-600 text-white rounded-r-lg px-6 py-3 transition duration-300 ease-in-out"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  )
}

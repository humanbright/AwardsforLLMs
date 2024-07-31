'use client'

import React, {useState, useRef, useEffect} from 'react'
import {v4 as uuidv4} from 'uuid'
import {RetellWebClient} from 'retell-client-js-sdk'

const agentId = '0822cbe326382cf5f2e22ac0fcc382f7'
const webClient = new RetellWebClient()

export default function Chat() {
  const [messages, setMessages] = useState([])
  const [inputMessage, setInputMessage] = useState('')
  const messagesEndRef = useRef(null)
  const [socket, setSocket] = useState(null)
  const clientId = useRef(uuidv4())
  const [isCalling, setIsCallActive] = useState(false)

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

    webClient.on('call_started', () => {
      console.log('call started')
    })

    webClient.on('call_ended', () => {
      console.log('call ended')
      setIsCallActive(false)
    })

    // When agent starts talking for the utterance
    // useful for animation
    webClient.on('agent_start_talking', () => {
      console.log('agent_start_talking')
    })

    // When agent is done talking for the utterance
    // useful for animation
    webClient.on('agent_stop_talking', () => {
      console.log('agent_stop_talking')
    })

    // Real time pcm audio bytes being played back, in format of Float32Array
    // only available when emitRawAudioSamples is true
    webClient.on('audio', (audio) => {
      // console.log(audio);
    })

    // Update message such as transcript
    webClient.on('update', (update) => {
      // console.log(update);
    })

    webClient.on('metadata', (metadata) => {
      // console.log(metadata);
    })

    webClient.on('error', (error) => {
      console.error('An error occurred:', error)
      // Stop the call
      webClient.stopCall()
    })

    webClient.on('update', (update) => {
      console.log('update', update)
      if (update.transcript) {
        setMessages(update.transcript)
      }
    })

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

  const toggleConversation = async () => {
    if (isCalling) {
      webClient.stopCall()
    } else {
      setIsCallActive(true)
      const registerCallResponse = await registerCall(agentId)
      if (registerCallResponse.access_token) {
        await webClient.startCall({
          accessToken: registerCallResponse.access_token,
        })
      }
    }
  }

  async function registerCall(agentId) {
    try {
      const response = await fetch(
        'https://fitting-correctly-lioness.ngrok-free.app/register-call-on-your-server',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            agentId: agentId,
          }),
        },
      )

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`)
      }

      const data = await response.json()
      return data
    } catch (err) {
      console.log(err)
      throw new Error(err)
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
            className="bg-blue-500 hover:bg-blue-600 text-black rounded-r-lg px-6 py-3 transition duration-300 ease-in-out"
          >
            Send
          </button>
        </div>
        <div className="mt-4 flex justify-center">
          <button
            onClick={toggleConversation}
            className={`${
              isCalling
                ? 'bg-red-500 hover:bg-red-600'
                : 'bg-green-500 hover:bg-green-600'
            } text-black rounded-lg px-6 py-3 transition duration-300 ease-in-out`}
          >
            {isCalling ? 'End Call' : 'Start Voice Call'}
          </button>
        </div>
      </div>
    </div>
  )
}

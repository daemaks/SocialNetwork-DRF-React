export interface IThread {
    id: number
    username: string
    community: string
    title: string
    content?: string
    image?: string
    created_at: Date
    updated_at: Date
}

export interface ICommunity {
    id: number
    tag: string
    title: string
    description?: string
    image?: string
    members: number[]
}
export interface ICommunity {
    id: number
    tag: string
    title: string
    description?: string
    image?: string
    members: number[]
}

export interface IThread {
    id: number
    username: string
    community: ICommunity
    title: string
    content?: string
    image?: string
    created_at: Date
    updated_at: Date
}

export interface ITag {
    id: number
    title: string
}
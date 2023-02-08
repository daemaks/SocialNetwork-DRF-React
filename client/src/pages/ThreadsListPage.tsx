import { useThreads } from "../hooks/threadsLoader";
import { Thread } from "../components/thread";
import Loader from "../layouts/loader";

export default function TreadsList() {
  const { loading, threads } = useThreads();
  return (
    <div className="flex flex-row justify-center mx-auto py-5 px-6">
      <div className="w-[640px]">
        {loading && <Loader />}
        {threads.map((thread) => (
          <Thread thread={thread} key={thread.id} />
        ))}
      </div>
      <div className="w-[320px] ml-6"></div>
    </div>
  );
}

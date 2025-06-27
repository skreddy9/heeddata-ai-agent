import { Metadata } from 'next';
import { redirect } from 'next/navigation';
import { isFlagEnabled } from '@/lib/feature-flags';

export const metadata: Metadata = {
  title: 'Create Agent | Heeddata AI Agent',
  description: 'Interactive agent playground powered by Heeddata AI Agent',
  openGraph: {
    title: 'Agent Playground | Heeddata AI Agent',
    description: 'Interactive agent playground powered by Heeddata AI Agent',
    type: 'website',
  },
};

export default async function NewAgentLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const agentPlaygroundEnabled = await isFlagEnabled('custom_agents');
  if (!agentPlaygroundEnabled) {
    redirect('/dashboard');
  }
  return <>{children}</>;
}

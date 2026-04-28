/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/12 20:12:08 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/15 13:38:06 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t num, size_t size)
{
	void	*ptr;

	if (size != 0 && num > SIZE_MAX / size)
	{
		return (NULL);
	}
	ptr = malloc(num * size);
	if (!ptr)
	{
		return (NULL);
	}
	ft_bzero(ptr, num * size);
	return (ptr);
}
